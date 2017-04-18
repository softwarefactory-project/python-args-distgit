%global srcname args

Name:           python-%{srcname}
Version:        0.1.0
Release:        3%{?dist}
Summary:        Argument Parsing for Humans

License:        BSD
URL:            https://github.com/kennethreitz/%{srcname}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
Argument Parsing for Humans.


%package -n python2-%{srcname}
Summary:        %{summary}
# Test requirements
BuildRequires:  python2-devel
BuildRequires:  python-nose
BuildRequires:  python-setuptools
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
Argument Parsing for Humans.


%prep
%autosetup -n %{srcname}-%{version}


%build
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}


# Upstream does not provide tests with 0.1.0, although
# the master branch does contain tests. With the next
# release, tests should be enabled.


%files -n python2-%{srcname}
%license LICENSE
%doc README.rst
%{python2_sitelib}/*


%changelog
* Fri Jul 08 2016 Jeremy Cline <jeremy@jcline.org> - 0.1.0-3
- Update spec for epel 7

* Wed Jul 06 2016 Jeremy Cline <jeremy@jcline.org> - 0.1.0-2
- Update spec based on review.

* Tue Jul 05 2016 Jeremy Cline <jeremy@jcline.org> - 0.1.0-1
- Initial commit
