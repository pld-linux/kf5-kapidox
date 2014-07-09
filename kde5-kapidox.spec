# TODO:
# - set ECM_MKSPECS_INSTALL_DIR in kde5-extra-cmake-modules
# - runtime Requires if any
# - python3 version
# - .pyo etc
%define         _state          stable
%define		orgname		kapidox

Summary:	Kapidox
Name:		kde5-%{orgname}
Version:	5.0.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/frameworks/%{version}/%{orgname}-%{version}.tar.xz
# Source0-md5:	682af5d0c1f01149106f28f9d82d09d9
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= 5.2.0
BuildRequires:	Qt5DBus-devel >= 5.2.0
BuildRequires:	Qt5Gui-devel >= 5.3.1
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel >= 5.2.0
BuildRequires:	Qt5X11Extras-devel >= 5.2.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kde5-extra-cmake-modules >= 1.0.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	sphinx-pdg
Requires:	graphviz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This framework contains scripts and data for building API
documentation (dox) in a standard format and style.

The Doxygen tool is used to do the actual documentation extraction and
formatting, but this framework provides a wrapper script to make
generating the documentation more convenient (including reading
settings from the target framework or other module) and a standard
template for the generated documentation.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DECM_MKSPECS_INSTALL_DIR=%{_libdir}/qt5/mkspecs/modules \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/depdiagram-generate
%attr(755,root,root) %{_bindir}/depdiagram-generate-all
%attr(755,root,root) %{_bindir}/depdiagram-prepare
%attr(755,root,root) %{_bindir}/kgenapidox
%attr(755,root,root) %{_bindir}/kgenframeworksapidox
%{py_sitescriptdir}/kapidox
%{py_sitescriptdir}/kapidox-*.egg-info
