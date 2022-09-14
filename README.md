# pdns-selinux-rpm
demo project, selinux module for pdns rpm on openshift 4

# build 

```bash

rpmbuild -bb ~/rpmbuild/SPECS/pdns-selinux.spec

```

# how to use

```bash

wget https://github.com/wangzheng422/pdns-selinux-rpm/releases/download/v0.0.1/pdns-selinux-0.0.1-0.el8.x86_64.rpm

dnf install pdns-selinux-0.0.1-0.el8.x86_64.rpm

```
