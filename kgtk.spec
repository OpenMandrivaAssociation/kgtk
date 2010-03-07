%define name	kgtk
%define oname	KGtk

Name:           %name
Version:        0.10.1
Release:        %mkrel 1
Summary:        KGtk - Allow to use KDE's file dialogs when run under KDE for GTK apps
Group:          Graphical desktop/KDE
License:        GPL
URL:            http://www.kde-apps.org/content/show.php/KGtk+%28Use+KDE+Dialogs+in+Gtk+Apps%29?content=36077
Source:	        %{oname}-%{version}.tar.bz2
Patch0:         KGtk-0.9.4-fix-libdir.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  kdelibs4-devel
BuildRequires:  gtk2-devel

%description
This is a quick-and-dirty LD_PRELOAD hack that allows *some* 
Gtk applications to use KDE's file dialogs when run under KDE. 

%files
%defattr(-,root,root,-)
%_bindir/kdialogd-wrapper
%_bindir/kdialogd4
%_bindir/kgtk-wrapper
%_bindir/kgtk2-wrapper
%_libdir/kgtk/libkgtk2.so

%{_datadir}/locale/*/LC_MESSAGES/kdialogd4.mo

#--------------------------------------------------------------------

%prep 
rm -rf $RPM_BUILD_ROOT
%setup -q -n %oname-%version
%patch0 -p1

%build
%cmake_kde4 -DKGTK_KDE4=true


%make

%install
cd build
%makeinstall_std
 
%clean
rm -rf $RPM_BUILD_ROOT
