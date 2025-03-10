#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	rencode
Summary:	Web safe object pickling/unpickling
Name:		python3-%{module}
Version:	1.0.6
Release:	2
License:	GPL v3//BSD
Group:		Libraries/Python
Source0:	https://github.com/aresch/rencode/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	5ad85007483c35d0d04c1e027a680f1c
URL:		https://github.com/aresch/rencode/
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The rencode module is a modified version of bencode from the
BitTorrent project.  For complex, heterogeneous data structures with
many small elements, r-encodings take up significantly less space than
b-encodings.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%{py3_sitedir}/%{module}/__pycache__
%{py3_sitedir}/%{module}-%{version}-py*.egg-info
