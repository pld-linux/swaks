Summary:	Swiss Army Knife SMTP
Summary(pl.UTF-8):	Szwajcarski scyzoryk SMTP
Name:		swaks
Version:	20201014.0
Release:	1
License:	GPL v2+
Group:		Applications
Source0:	http://www.jetmore.org/john/code/swaks/files/%{name}-%{version}.tar.gz
# Source0-md5:	fc4f2bf1df88b38a2392d2e24c52754e
URL:		http://jetmore.org/john/code/
BuildRequires:	perl-tools-pod
BuildRequires:	rpm-perlprov
Suggests:	perl-perldoc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Swiss Army Knife SMTP; Command line SMTP testing, including TLS and
AUTH.

%description -l pl.UTF-8
Narzędzie do testowania SMTP, łącznie z TLS i uwierzytelnianiem.

%prep
%setup -q

%build
pod2man %{name} > swaks.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a swaks.1 $RPM_BUILD_ROOT%{_mandir}/man1/swaks.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt doc/*
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/swaks.1*
