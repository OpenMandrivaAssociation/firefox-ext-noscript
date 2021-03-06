Summary: Firefox extension that protects against XSS and Clickjacking attacks
Name: firefox-ext-noscript
Version: 2.0.9.8
Release: 3
License: MPL
Group:	Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/722/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/722/noscript-%{version}-sm+fx+fn.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_version}
BuildRequires: firefox-devel
Buildarch: noarch

%description
The best security you can get in a web browser!
Allow active content to run only from sites you trust, and protect yourself
against XSS and Clickjacking attacks.

Winner of the "2006 PC World World Class Award", this tool provides extra
protection to your Firefox. 
It allows JavaScript, Java and other executable content to run only from
trusted domains of your choice, e.g. your home-banking web site, guarding your
"trust boundaries" against cross-site scripting attacks (XSS), cross-zone DNS
rebinding / CSRF attacks (router hacking), and Clickjacking attempts, thanks to
its unique ClearClick technology.

Such a preemptive approach prevents exploitation of security vulnerabilities
(known and even unknown!) with no loss of functionality... 
Experts do agree: Firefox is really safer with NoScript ;-)

%prep
%setup -q -c -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{firefox_extdir}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{firefox_extdir}/"
mkdir -p "%{buildroot}$extdir"
cp -af %SOURCE0 "%{buildroot}$extdir/$hash.xpi"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{firefox_extdir}


%changelog
* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 2.0.9.8-1mdv2011.0
+ Revision: 640553
- 2.0.9.8 final

* Tue Feb 15 2011 Thierry Vignaud <tv@mandriva.org> 2.0.9.8-0.1rc3
+ Revision: 637878
- new prerelease

* Fri Jan 28 2011 Funda Wang <fwang@mandriva.org> 2.0.9.6-2
+ Revision: 633596
- drop hard version req

* Wed Jan 26 2011 Thierry Vignaud <tv@mandriva.org> 2.0.9.6-1
+ Revision: 632898
- new release

* Wed Jan 19 2011 Thierry Vignaud <tv@mandriva.org> 2.0.9.3-2
+ Revision: 631669
- prevent need to rebuild for every new firefox
- only package .xpi

* Wed Jan 05 2011 Thierry Vignaud <tv@mandriva.org> 2.0.9.3-1mdv2011.0
+ Revision: 628866
- new release

* Mon Nov 29 2010 Thierry Vignaud <tv@mandriva.org> 2.0.7-1mdv2011.0
+ Revision: 603137
- new release

* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 2.0.4-2mdv2011.0
+ Revision: 597378
- rebuild for new firefox

* Sun Nov 07 2010 Thierry Vignaud <tv@mandriva.org> 2.0.4-1mdv2011.0
+ Revision: 594630
- import firefox-ext-noscript

