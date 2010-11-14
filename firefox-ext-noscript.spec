%define _mozillaextpath %{firefox_mozillapath}/extensions
%define debug_package %{nil}

Summary: Firefox extension that protects against XSS and Clickjacking attacks
Name: firefox-ext-noscript
Version: 2.0.4
Release: %mkrel 2
License: MPL
Group:	Networking/WWW
URL: https://addons.mozilla.org/en-US/firefox/addon/722/
Source: http://releases.mozilla.org/pub/mozilla.org/addons/722/noscript-%{version}-fx+sm+fn.xpi
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
Requires: firefox = %{firefox_epoch}:%{firefox_version}
BuildRequires: firefox-devel

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

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_mozillaextpath}

hash="$(sed -n '/.*em:id="\(.*\)"/{s//\1/p;q}' install.rdf)"
if [ -z "$hash" ]; then
    hash="$(sed -n '/.*em:id>\(.*\)<\/em:id>.*/{s//\1/p;q}' install.rdf)"
fi
if [ -z "$hash" ]; then
    echo "Failed to find plugin hash."
    exit 1
fi
extdir="%{_mozillaextpath}/$hash"
mkdir -p "%{buildroot}$extdir"
cp -af * "%{buildroot}$extdir/"

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%dir %firefox_mozillapath
%{_mozillaextpath}


