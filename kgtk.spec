%define name    kgtk
%define oname    KGtk

Name:           %name
Version:        0.9.4
Release:        %mkrel 1
Summary:        KGtk - Allow to use KDE's file dialogs when run under KDE for GTK apps
Group:          Graphical desktop/KDE
License:        GPL
URL:            http://www.kde-apps.org/content/show.php/KGtk+%28Use+KDE+Dialogs+in+Gtk+Apps%29?content=36077
Source:	        %{oname}-%{version}.tar.bz2
BuildRequires:  kdelibs-devel
BuildRequires:  cmake
BuildRequires:  gtk2-devel

%description
This is a quick-and-dirty LD_PRELOAD hack that allows *some* 
Gtk applications to use KDE's file dialogs when run under KDE. 

%files
%defattr(-,root,root,-)
%_bindir/kdialogd-wrapper
%_bindir/kdialogd3
%_bindir/kgtk-wrapper
%_bindir/kgtk2-wrapper
%_bindir/kqt3-wrapper
%_libdir/kgtk/libkgtk2.so
%_libdir/kgtk/libkqt3.so

%{_datadir}/locale/*/LC_MESSAGES/kdialogd3.mo

#--------------------------------------------------------------------

%prep 
rm -rf $RPM_BUILD_ROOT
%setup -q -n %oname-%version


%build

mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=%_prefix \
%if "%_lib" != "lib"
        -DLIB_SUFFIX=64
%endif


%make

%install
cd build
%makeinstall_std
 
%clean
rm -rf $RPM_BUILD_ROOT
