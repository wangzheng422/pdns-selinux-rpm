# pdns-selinux-rpm
demo project, selinux module for pdns rpm on openshift 4

# build 

```bash

rpmbuild -bb ~/rpmbuild/SPECS/pdns-selinux.spec

```

# how to use

```bash

wget https://github.com/wangzheng422/distribution-rpm/releases/download/v2.8.1-0/docker-distribution-2.8.1-0.el8.x86_64.rpm

dnf install pdns-selinux-0.0.1-0.el8.x86_64.rpm

```
