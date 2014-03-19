# Disable the build of a debug package
%define		_enable_debug_package	0
%define		debug_package		%{nil}
%define		__os_install_post	/usr/lib/rpm/brp-compress %{nil}
%define		squeak_ver		4.10.2-2614

Name:		scratch
Version:	1.4.0.7
Release:	2
Summary:	Programming system and content development tool
Group:		Education
Group:		Development/Other
License:	MIT
URL:		http://scratch.mit.edu
Source0:	http://info.scratch.mit.edu/sites/infoscratch.media.mit.edu/files/file/scratch-1.4.0.7.src.tar.gz
Source1:	scratch.rpmlintrc
Patch0:		scratch_locale.patch
Patch1:		scratch-1.4.0.7-sduino-find_serial_ports.patch
BuildRequires:	libv4l-devel
BuildRequires:	pkgconfig(pangocairo)
Requires:	squeak-vm

%description
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

%prep
%setup -q -n %{name}-%{version}.src
%patch0 -p0
%patch1 -p1

rm -f Plugins/* Plugins64/* App/scratch_squeak_vm

%build

make

%install
install -d %{buildroot}%{_libdir}/%{name}/Plugins
install -m 644 Scratch.{image,ini} %{buildroot}%{_libdir}/%{name}
install -m 644 Plugins/* %{buildroot}%{_libdir}/%{name}/Plugins

install -d %{buildroot}%{_datadir}/%{name}
cp -fpR Help locale Media Projects %{buildroot}%{_datadir}/%{name}

install -d %{buildroot}%{_docdir}/%{name}
ln -sf %{_datadir}/%{name}/Help %{buildroot}%{_docdir}/%{name}/Help
install -m 644 {ACKNOWLEDGEMENTS,KNOWN-BUGS,LICENSE} %{buildroot}%{_docdir}/%{name}

install -d %{buildroot}%{_mandir}/man1
install -m 644 src/man/scratch.1.gz %{buildroot}%{_mandir}/man1

install -d %{buildroot}%{_datadir}/applications
install -m 644 src/%{name}.desktop %{buildroot}%{_datadir}/applications

mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{48x48,128x128}/{apps,mimetypes}
install -m 644 src/icons/48x48/scratch.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/icons/128x128/scratch.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -m 644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -d %{buildroot}%{_datadir}/mime/packages
install -m 644 src/%{name}.xml %{buildroot}%{_datadir}/mime/packages

install -d %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/sh
# Squeakvm wrapper to load Scratch image.
#------------------------------------------------------------

/usr/bin/squeak \
-plugins %{_libdir}/scratch/Plugins:%{_libdir}/squeak/%{squeak_ver} \
-vm-sound-ALSA \
%{_libdir}/scratch/Scratch.image "\${@}"
EOF
chmod +x %{buildroot}%{_bindir}/%{name}

chmod -R 0755 %{buildroot}/%{_datadir}/%{name}/Media
chmod -R 0755 %{buildroot}/%{_datadir}/%{name}/Projects
chmod -R 0755 %{buildroot}/%{_datadir}/%{name}/Help

%files
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%doc %{_docdir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*
