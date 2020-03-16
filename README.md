To fix: To build you need to manually clone and generate the tar.gz expected by the spec file.
Spec files uploaded to Fedor's repo auto download the source code. I would fix this later.

```
git clone https://github.com/wybiral/torgo.git
mv torgo/ torgo-a19a6c8a50489e2fdf37223edc5f1284bb965308
tar zcf torgo-a19a6c8a50489e2fdf37223edc5f1284bb965308.tar.gz torgo-a19a6c8a50489e2fdf37223edc5f1284bb965308
```

To build this package you would need to install the `golang-x-crypto-devel` package.

Building the package:
```
fedpkg --release f31 local
```
