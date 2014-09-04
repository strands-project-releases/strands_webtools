cd /tmp

rm -rf httpd-2.2.20

# Checkout apache source
svn checkout http://svn.apache.org/repos/asf/httpd/httpd/tags/2.2.20/ httpd-2.2.20 
# Get patch and apply it
wget http://cafarelli.fr/gentoo/apache-2.2.24-wstunnel.patch
cd httpd-2.2.20
patch -p1 < ../apache-2.2.24-wstunnel.patch
# Build Apache 
svn co http://svn.apache.org/repos/asf/apr/apr/branches/1.4.x srclib/apr
svn co http://svn.apache.org/repos/asf/apr/apr-util/branches/1.3.x srclib/apr-util
./buildconf
./configure --enable-proxy=shared --enable-proxy_wstunnel=shared
make
# Copy the module and recompiled mod_proxy (for new symbols) to the ubuntu apache installation and update the permissions to match the other modules
sudo cp modules/proxy/.libs/mod_proxy{_wstunnel,}.so /usr/lib/apache2/modules/
sudo chmod 644 /usr/lib/apache2/modules/mod_proxy{_wstunnel,}.so
echo -e "# Depends: proxy\nLoadModule proxy_wstunnel_module /usr/lib/apache2/modules/mod_proxy_wstunnel.so" | sudo tee -a /etc/apache2/mods-available/proxy_wstunnel.load


