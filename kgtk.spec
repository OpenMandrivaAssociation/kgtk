%define name	kgtk
%define oname	KGtk

Name:           %name
Version:        0.10.1
Release:        %mkrel 2
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


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.10.1-2mdv2011.0
+ Revision: 612599
- the mass rebuild of 2010.1 packages

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.10.1-1mdv2010.1
+ Revision: 515352
- update to 0.10.1
- drop an old patch, applied upstream.

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Mar 06 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.10.0-1mdv2009.1
+ Revision: 349614
- Fix build
- New version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.4-2mdv2008.1
+ Revision: 177677
- [BUGFIX] Fix preload error (Bug #37936)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill extra spacing at top of description

* Fri Dec 07 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.9.4-1mdv2008.1
+ Revision: 116104
- Fix install on x86_64
- import kgtk


