#
# Conditional build:
%bcond_with	tests	# perform "make test". starts test httpd service

%define		pdir	Apache
%define		pnam	Scoreboard
%include	/usr/lib/rpm/macros.perl
Summary:	Apache::Scoreboard - Perl interface to the Apache scoreboard structure
Summary(pl.UTF-8):	Apache::Scoreboard - perlowy interfejs do struktury scoreboard Apache'a
Name:		perl-Apache-Scoreboard
Version:	2.09.2
Release:	3
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	df133feb853c4ef743557e6621adcc3f
URL:		http://search.cpan.org/dist/Apache-Scoreboard/
BuildRequires:	apache-mod_perl-devel
BuildRequires:	apr-devel >= 1:1.0
BuildRequires:	apr-util-devel >= 1:1.0
BuildRequires:	perl-Apache-Test
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-mod_perl
%if %{with tests}
BuildRequires:	perl-Chart-PNGgraph
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache keeps track of server activity in a structure known as the
scoreboard. There is a slot in the scoreboard for each child server,
containing information such as status, access count, bytes served and
cpu time. This same information is used by mod_status to provide
current server statistics in a human readable form.

%description -l pl.UTF-8
Apache śledzi aktywność serwera w strukturze znanej jako scoreboard. W
scoreboard znajduje się slot dla każdego serwera potomnego,
zawierający informacje takie jak stan, liczba klientów, wysłanych
bajtów i zajęty czas procesora. Te same informacje są używane przez
mod_status do udostępniania aktualnych statystyk w postaci czytelnej
dla człowieka.

%prep
%setup -q -n %{pdir}-%{pnam}-2.09

%build
INC="-I/usr/include/apache $(apr-1-config --includes) $(apu-1-config --includes)"
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="$INC"
cd Dummy
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="$INC"
cd ..
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Apache/Scoreboard/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Apache/*.pm
%dir %{perl_vendorarch}/auto/Apache
%dir %{perl_vendorarch}/auto/Apache/Scoreboard
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Scoreboard/*.so
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
