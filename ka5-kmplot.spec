#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.04.3
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kmplot
Summary:	kmplot
Name:		ka5-%{kaname}
Version:	22.04.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	a4044e659ddaa526e5429de612c3c8d3
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kguiaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KmPlot is a program to draw graphs, their integrals or derivatives. It
supports different systems of coordinates like the Cartesian or the
polar coordinate system. The graphs can be colorized and the view is
scalable, so that you are able to zoom to the level you need.

%description -l pl.UTF-8
KmPlot jest programem rysującym wykresy funkcji, całek i pochodnych.
Obsługuje różne układy współrzędnych, np. Kartezjański czy biegunowy.
Wykresy są kolorowane i skalowalne, tak że jesteś w stanie powiększyć
je do poziomu, którego potrzebujesz.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmplot
%{_libdir}/qt5/plugins/kf5/parts/kmplotpart.so
%{_desktopdir}/org.kde.kmplot.desktop
%{_datadir}/config.kcfg/kmplot.kcfg
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.KmPlot.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.MainDlg.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.Parser.xml
%{_datadir}/dbus-1/interfaces/org.kde.kmplot.View.xml
%{_iconsdir}/hicolor/128x128/apps/kmplot.png
%{_iconsdir}/hicolor/16x16/apps/kmplot.png
%{_iconsdir}/hicolor/22x22/apps/kmplot.png
%{_iconsdir}/hicolor/32x32/apps/kmplot.png
%{_iconsdir}/hicolor/48x48/apps/kmplot.png
%{_iconsdir}/hicolor/64x64/apps/kmplot.png
%{_iconsdir}/hicolor/scalable/apps/kmplot.svgz
%{_datadir}/kservices5/kmplot_part.desktop
%dir %{_datadir}/kxmlgui5/kmplot
%{_datadir}/kxmlgui5/kmplot/kmplot_part.rc
%{_datadir}/kxmlgui5/kmplot/kmplot_part_readonly.rc
%{_datadir}/kxmlgui5/kmplot/kmplot_shell.rc
%{_datadir}/metainfo/org.kde.kmplot.appdata.xml
%lang(ca) %{_mandir}/ca/man1/kmplot.1*
%lang(de) %{_mandir}/de/man1/kmplot.1*
%lang(es) %{_mandir}/es/man1/kmplot.1*
%lang(et) %{_mandir}/et/man1/kmplot.1*
%lang(fr) %{_mandir}/fr/man1/kmplot.1*
%lang(gl) %{_mandir}/gl/man1/kmplot.1*
%lang(it) %{_mandir}/it/man1/kmplot.1*
%lang(C) %{_mandir}/man1/kmplot.1*
%lang(nl) %{_mandir}/nl/man1/kmplot.1*
%lang(pl) %{_mandir}/pl/man1/kmplot.1*
%lang(pt) %{_mandir}/pt/man1/kmplot.1*
%lang(pt_BR) %{_mandir}/pt_BR/man1/kmplot.1*
%lang(ru) %{_mandir}/ru/man1/kmplot.1*
%lang(sv) %{_mandir}/sv/man1/kmplot.1*
%lang(uk) %{_mandir}/uk/man1/kmplot.1*
