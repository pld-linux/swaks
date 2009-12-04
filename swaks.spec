#
%include	/usr/lib/rpm/macros.perl
Summary:	Swiss Army Knife SMTP
Summary(pl.UTF-8):	Szwajcarski scyzoryk SMTP
Name:		swaks
Version:	20061116.0
Release:	1
License:	GPL v2+
Group:		Applications
# http://jetmore.org/john/code/swaks
Source0:	%{name}.pl
URL:		http://jetmore.org/john/code/#swaks
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
%setup -q -c -T

%build
pod2man %{SOURCE0} > swaks.1
pod2text %{SOURCE0} > swaks.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a swaks.1 $RPM_BUILD_ROOT%{_mandir}/man1/swaks.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc swaks.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/swaks.1*
