# TODO:
# - runtime Requires if any
# - python3 version
# - .pyo etc
%define         kdeframever     5.56
%define         qtver           5.9.0
%define         kfname          kapidox
Summary:	Kapidox
Name:		kf5-%{kfname}
Version:	5.56.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	d6d7a6c003dfdc22c5b9671af3985af4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.2.0
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= %{version}
BuildRequires:	ninja
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sphinx-pdg
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	graphviz
Requires:	kf5-dirs
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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/depdiagram-generate
%attr(755,root,root) %{_bindir}/depdiagram-generate-all
%attr(755,root,root) %{_bindir}/depdiagram-prepare
%attr(755,root,root) %{_bindir}/kapidox_generate
#%%attr(755,root,root) %{_bindir}/kgenapidox
#%%attr(755,root,root) %{_bindir}/kgenframeworksapidox
%{py_sitedir}/kapidox
%{py_sitedir}/kapidox-*.egg-info
%{_mandir}/man1/depdiagram-generate-all.1*
%{_mandir}/man1/depdiagram-generate.1*
%{_mandir}/man1/depdiagram-prepare.1*
#%%{_mandir}/man1/kgenapidox.1*
#%%{_mandir}/man1/kgenframeworksapidox.1*
