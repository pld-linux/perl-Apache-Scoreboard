# 
# Conditional build:
# Can't get tests to work. Apache::Test doesn't find mod_status.
%bcond_with	tests	# don't perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Scoreboard
Summary:	Apache::Scoreboard - Perl interface to the Apache scoreboard structure
Summary(pl):	Apache::Scoreboard - perlowy interfejs do struktury scoreboard Apache'a
Name:		perl-Apache-Scoreboard
Version:	2.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	461284a6cf13cf20146b6e8d7f766615
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	perl-devel >= 1:5.8.0
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

%description -l pl
Apache ¶ledzi aktywno¶æ serwera w strukturze znanej jako scoreboard.
W scoreboard znajduje siê slot dla ka¿dego serwera potomnego,
zawieraj±cy informacje takie jak stan, liczba klientów, wys³anych
bajtów i zajêty czas procesora. Te same informacje s± u¿ywane przez
mod_status do udostêpniania aktualnych statystyk w postaci czytelnej
dla cz³owieka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor \
	INC="-I/usr/include/apache $(apr-1-config --includes) $(apu-1-config --includes)"
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Apache/*.pm
%dir %{perl_vendorarch}/auto/Apache/Scoreboard
%attr(755,root,root) %{perl_vendorarch}/auto/Apache/Scoreboard/*.so
%{perl_vendorarch}/auto/Apache/Scoreboard/*.bs
# Isn't built. What's this anyway?
#%dir %{perl_vendorarch}/auto/Apache/DummyScoreboard
#%attr(755,root,root) %{perl_vendorarch}/auto/Apache/DummyScoreboard/*.so
#%{perl_vendorarch}/auto/Apache/DummyScoreboard/*.bs
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
