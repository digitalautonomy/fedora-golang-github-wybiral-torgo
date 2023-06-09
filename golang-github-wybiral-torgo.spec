# Generated by go2rpm 1
%bcond_without check

# https://github.com/wybiral/torgo
%global goipath         github.com/wybiral/torgo
%global commit          5fd9910eab3125e20055492e54cdee2e11574aa1

%gometa

%global common_description %{expand:
A Golang library for Tor.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Version:        0
Release:        0.2%{?dist}
Summary:        A Golang library for Tor

License:        GPL-3.0-only
# FIXME: Upstream uses unknown SPDX tag GPL-3.0-only!
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/crypto/ed25519)
BuildRequires:  golang(golang.org/x/crypto/sha3)
BuildRequires:  golang(golang.org/x/net/proxy)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Fri Apr 28 17:00:00 -05 2023 CAD <fedora@autonomia.digital> - 0-0.2.20201209git5fd9910
- Update torgo version and build for more fedora versions
* Fri Mar 13 16:35:29 -05 2020 rafael <rafael@autonomia.digital> - 0-0.1.20200313gita19a6c8
- Initial package


