%define oname KGtk

Summary:	KGtk - Allow to use KDE's file dialogs when run under KDE for GTK apps
Name:		kgtk
Version:	0.11.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde-apps.org/content/show.php/KGtk+%28Use+KDE+Dialogs+in+Gtk+Apps%29?content=36077
Source0:	%{oname}-%{version}.tar.bz2
Source10:	%{name}.rpmlintrc
Patch0:		kgtk-0.11.0-fix-libdir.patch
Patch1:		kgtk-0.11.0-include.patch
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
This is a quick-and-dirty LD_PRELOAD hack that allows *some*
Gtk applications to use KDE's file dialogs when run under KDE.

%files -f kdialogd4.lang
%{_kde_bindir}/kgtk-wrapper
%{_kde_libdir}/kde4/libexec/kdialogd4
%{_kde_libdir}/kgtk/libkgtk2.so
%{_kde_libdir}/kgtk/libkgtk3.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p0

%build
%cmake_kde4 -DKGTK_KDE4=true
%make

%install
%makeinstall_std -C build

%find_lang kdialogd4

