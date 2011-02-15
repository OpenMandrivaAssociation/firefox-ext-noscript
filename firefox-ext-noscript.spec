%define pre rc3
Summary: Firefox extension that protects against XSS and Clickjacking attacks
Name: firefox-ext-noscript
Version: 2.0.9.8
Release: %mkrel 0.1%pre
License: MPL
Group:	Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/722/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/722/noscript-%{version}%{pre}-sm+fx+fn.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox >= %{firefox_epoch}:%{firefox_version}
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


