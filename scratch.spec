Name:           scratch
Version:        1.4.0.7
Release:        11
Summary:        Programming language learning environment for stories, games, music and art

Group:          Education
License:        GPLv2 and ASL 2.0 and MIT and CC-BY-SA
URL:            https://scratch.mit.edu
Source0:        http://download.scratch.mit.edu/%{name}-%{version}.src.tar.gz
# The following source file is not used in the build process, but together
# with Scratch.image and src/Scratch.changes comprises the preferred means
# of modification -- see the included README. This file is under the MIT
# and Apache 2.0 docs.
Source1:        http://ftp.squeak.org/2.0/SqueakV2.sources.gz
Source2:        50-wedo.rules
Source3:	scratch.appdata.xml
Patch0:         scratch-1.4.0.7-use-fedora-squeak.patch
Patch1:         scratch-1.4.0.6-desktopfile-semicolon.patch

BuildArch:	noarch

BuildRequires: desktop-file-utils

Requires:       scratch-image
Requires:       scratch-media, scratch-projects
Requires:       scratch-help, scratch-i18n

%description
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

As young people create and share Scratch projects, they learn important
mathematical and computational ideas, while also learning to think
creatively, reason systematically, and work collaboratively.

This package brings in all of the various subpackages which comprise the
full Scratch distribution.


%package image
Summary: The Scratch programming environment
License: GPLv2 and ASL 2.0 and MIT
Requires: squeak-vm
BuildArch: noarch

%description image
Scratch is a programming language that makes it easy to create your own
interactive stories, animations, games, music, and art -- and share your
creations on the web.

This package contains the core Scratch programming environment.


%package help
Summary: Documentation for the Scratch programming language
License: CC-BY-SA
BuildArch: noarch

%description help
This package contains HTML and PDF documentation for scratch. The HTML
documentation is referenced in the Scratch menu, and the PDFs are linked
from that.


%package media
Summary: The standard distribution of sprites and media for Scratch
License: CC-BY-SA
BuildArch: noarch

%description media
This package contains the standard collection of images and sounds for the
Scratch programming language.


%package projects
Summary: The standard distribution of Scratch projects
License: CC-BY-SA
BuildArch: noarch

%description projects
This package contains the standard collection of sample projects for the
Scratch programming language.


%package i18n
Summary: Translations for the Scratch programming environment
License: GPLv2
BuildArch: noarch

%description i18n
This package contains international support for the Scratch programming
environment. If it is not installed, Scratch will only be available in
English


%prep
%setup -q -n %{name}-%{version}.src
%autopatch -p1

%build
# since the Squeak VM version 4.10.2.2593 and greater includes all the
# plugins previously included as part of Scratch, we don't need to build
# anything here.


%install
install -m 755 -d %{buildroot}%{_datadir}/%{name}
install -m 644 Scratch.image %{buildroot}%{_datadir}/%{name}/
install -m 644 Scratch.ini %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Help/en/images
install -m 644 Help/en/*.pdf %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.html %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/
install -m 644 Help/en/images/*.gif %{buildroot}%{_datadir}/%{name}/Help/en/images/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/locale
install -m 644 locale/* %{buildroot}%{_datadir}/%{name}/locale/

cp -R Media  %{buildroot}%{_datadir}/%{name}/

install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Animation
install -m 644 Projects/Animation/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Animation/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Games
install -m 644 Projects/Games/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Games/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Greetings
install -m 644 Projects/Greetings/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Greetings/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art
install -m 644 Projects/Interactive\ Art/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Interactive\ Art/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance
install -m 644 Projects/Music\ and\ Dance/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Music\ and\ Dance/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Names
install -m 644 Projects/Names/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Names/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors
install -m 644 Projects/Sensors\ and\ Motors/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Sensors\ and\ Motors/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Simulations
install -m 644 Projects/Simulations/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Simulations/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up
install -m 644 Projects/Speak\ Up/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Speak\ Up/
install -m 755 -d %{buildroot}%{_datadir}/%{name}/Projects/Stories
install -m 644 Projects/Stories/*.sb %{buildroot}%{_datadir}/%{name}/Projects/Stories/

install -m 755 -d %{buildroot}%{_bindir}/
install -m 755 src/scratch %{buildroot}%{_bindir}/

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 src/man/scratch.1.gz %{buildroot}%{_mandir}/man1/

install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install --dir=%{buildroot}%{_datadir}/applications src/%{name}.desktop

install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -m 644 src/icons/48x48/scratch.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/apps
install -m 644 src/icons/128x128/scratch.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes
install -m 644 src/icons/48x48/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/48x48/mimetypes/
install -m 755 -d %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes
install -m 644 src/icons/128x128/gnome-mime-application-x-scratch-project.png %{buildroot}%{_datadir}/icons/hicolor/128x128/mimetypes/

install -m 755 -d %{buildroot}%{_datadir}/mime/packages
install -m 644 src/%{name}.xml %{buildroot}%{_datadir}/mime/packages/

install -m 755 -d %{buildroot}%{_udevrulesdir}
install -m 644 %{SOURCE2} %{buildroot}%{_udevrulesdir}/

mkdir -p %{buildroot}%{_datadir}/appdata
cp -a %{SOURCE3} %{buildroot}%{_datadir}/appdata/
chmod -R 755 %{buildroot}/%{_datadir}/%{name}/Media/

%post
/usr/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/touch --no-create %{_datadir}/mime/packages &> /dev/null || :


%files
%doc LICENSE gpl-2.0.txt TRADEMARK_POLICY
%doc KNOWN-BUGS ACKNOWLEDGEMENTS NOTICE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*.1*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/icons/hicolor/48x48/mimetypes/*
%{_datadir}/icons/hicolor/128x128/apps/*
%{_datadir}/icons/hicolor/128x128/mimetypes/*
%{_udevrulesdir}/50-wedo.rules
%{_datadir}/appdata/%{name}.appdata.xml

%files image
%doc LICENSE gpl-2.0.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Scratch.image
%{_datadir}/%{name}/Scratch.ini

%files help
%doc LICENSE
%dir %{_datadir}/%{name}/Help
%{_datadir}/%{name}/Help/*

%files media
%doc LICENSE
%dir %{_datadir}/%{name}/Media
%{_datadir}/%{name}/Media/*

%files projects
%doc LICENSE
%dir %{_datadir}/%{name}/Projects
%{_datadir}/%{name}/Projects/*

%files i18n
%doc LICENSE gpl-2.0.txt
%{_datadir}/%{name}/locale
