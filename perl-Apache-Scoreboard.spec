%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	Scoreboard
Summary:	Apache::Scoreboard - Perl interface to the Apache scoreboard structure
Summary(pl):	Apache::Scoreboard - perlowy interfejs do struktury scoreboard Apache'a
Name:		perl-Apache-Scoreboard
Version:	0.10
Release:	5
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
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

# %package -n apache-mod_scoreboard_send
# Should mod_scoreboard_send be built, too?  Here, or from a separate spec?

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitearch}/Apache/*.pm
%dir %{perl_sitearch}/auto/Apache/Scoreboard
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Scoreboard/*.so
%{perl_sitearch}/auto/Apache/Scoreboard/*.bs
%dir %{perl_sitearch}/auto/Apache/DummyScoreboard
%attr(755,root,root) %{perl_sitearch}/auto/Apache/DummyScoreboard/*.so
%{perl_sitearch}/auto/Apache/DummyScoreboard/*.bs
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
