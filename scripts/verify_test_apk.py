#!/usr/bin/env python3
"""Extract and verify the exact previously tested APK before prerelease publication."""
import hashlib,json,os,re,shutil,subprocess,zipfile
from pathlib import Path

def verify(root=Path('.')):
    data=json.loads((root/'test-release.json').read_text())
    version=data['versionName']
    assert re.fullmatch(r'[0-9A-Za-z._-]+',version) and '-audit' in version
    assert data['channel']=='manual-test' and data['stableFeedChanged'] is False
    name='DriveCanvas-'+version+'.apk';assert data['apk']==name
    folder=root/'tests'/version;apk=folder/name
    with zipfile.ZipFile(folder/(name+'.zip')) as bundle:
        assert bundle.namelist()==[name]
        assert bundle.getinfo(name).file_size==data['apkSizeBytes']
        with bundle.open(name) as source,apk.open('wb') as target:shutil.copyfileobj(source,target)
    assert apk.stat().st_size==data['apkSizeBytes']
    assert hashlib.sha256(apk.read_bytes()).hexdigest()==data['sha256']
    sdk=Path(os.environ['ANDROID_HOME'])/'build-tools/34.0.0'
    cert=subprocess.check_output([str(sdk/'apksigner'),'verify','--print-certs',str(apk)],text=True)
    pinned=json.loads((root/'.github/android-signing-identity.json').read_text())['certificateSha256']
    assert re.findall(r'Signer #\d+ certificate SHA-256 digest: (\w+)',cert)==[pinned]
    assert data['certificateSha256']==pinned
    badging=subprocess.check_output([str(sdk/'aapt'),'dump','badging',str(apk)],text=True)
    assert "package: name='com.drivecanvas.app' versionCode='"+str(data['versionCode'])+"' versionName='"+version+"'" in badging
    assert data['apkUrl']=='https://github.com/mdqr69/DriveCanvas-Releases/releases/download/v'+version+'/'+name
    assert data['androidTests']==dict(tests=540,failures=0,errors=0,skipped=0)
    assert data['lintErrors']==0
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'],'a') as output:output.write('tag=v'+version+'\napk='+str(apk)+'\nnotes='+str(folder/'TEST_NOTES.md')+'\n')
    print('Verified exact signed test APK:',version,data['sha256'])

if __name__=='__main__':verify()
