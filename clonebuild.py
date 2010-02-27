import os, shutil, tarfile, os.path as osp

package = osp.basename(os.getcwd())
mod = __import__(package)
parentdir = osp.join(os.getcwd(), osp.pardir)
package_ver = '%s-%s' % (package, mod.__version__)

os.chdir(parentdir)
if osp.isdir(package_ver):
    shutil.rmtree(package_ver)

os.system('hg clone %s %s' % (package, package_ver))

tar = tarfile.open("%s.tar.gz" % package_ver, "w|gz")
tar.add(package_ver, recursive=True,
        exclude=lambda fn: osp.relpath(fn, package_ver).startswith('.hg'))
tar.close()

os.chdir(package_ver)
build_cmd = 'python setup.py build_ext --compiler=mingw32'
os.system('%s bdist_wininst' % build_cmd)
os.system('%s bdist_egg' % build_cmd)

os.chdir(parentdir)
dist = osp.join(package_ver, "dist")
info = osp.join(package_ver, "%s.egg-info" % package)
names = ["%s.win32.exe" % package_ver,
         "%s-py2.6.egg" % package_ver]
for name in names:
    shutil.copy(osp.join(dist, name), osp.join(parentdir, name))
name = "PKG-INFO"
shutil.copy(osp.join(info, name), osp.join(parentdir, "%s-info" % package_ver))
shutil.rmtree(package_ver)
