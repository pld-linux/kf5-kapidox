#
# Conditional build:
%bcond_with	tests		# build with tests
# TODO:
# - runtime Requires if any
# - python3 version
# - .pyo etc
%define		kdeframever	5.116
%define		qtver		5.15.2
%define		kfname		kapidox
Summary:	Kapidox
Name:		kf5-%{kfname}
Version:	5.116.0
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	a0565ce340834aff5fee487faacd76e9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.2.0
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	cmake >= 3.16
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	graphviz
Requires:	kf5-dirs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
This framework contains scripts and data for building API
documentation (dox) in a standard format and style.

The Doxygen tool is used to do the actual documentation extraction and
formatting, but this framework provides a wrapper script to make
generating the documentation more convenient (including reading
settings from the target framework or other module) and a standard
template for the generated documentation.

%prep
%setup -q -n %{kfname}-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/depdiagram_generate_all
%attr(755,root,root) %{_bindir}/kapidox-depdiagram-generate
%attr(755,root,root) %{_bindir}/kapidox-depdiagram-prepare
%attr(755,root,root) %{_bindir}/kapidox-generate
%{py3_sitescriptdir}/kapidox/
%{py3_sitescriptdir}/kapidox-*.egg-info
