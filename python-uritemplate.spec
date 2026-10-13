Name:		python-uritemplate
Version:	4.2.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/u/uritemplate/uritemplate-%{version}.tar.gz
Summary:	Implementation of RFC 6570 URI Templates
URL:		https://pypi.org/project/uritemplate/
License:	BSD 3-Clause License or Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildSystem:	python
BuildArch:	noarch

%description
Implementation of RFC 6570 URI Templates

%files
%{py_sitedir}/uritemplate
%{py_sitedir}/uritemplate-*.*-info
