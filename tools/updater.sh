crd=pwd
cd /tmp/
git clone https://github.com/AdolfMacro/lordrat.git
sudo -u root cp -R lordrat/* /usr/src/lordRAT/
sudo -u root rm -rf lordrat
cd $prc
