%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	Scoreboard
Summary:	Apache::Scoreboard - Perl interface to the Apache scoreboard structure
#Summary(pl):	
Name:		perl-Apache-Scoreboard
Version:	0.10
Release:	2
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# required by example scripts
%define		_noautoreq	'perl(Chart::PNGgraph::bars)' 'perl(Chart::PNGgraph::lines)' 'perl(Chart::PNGgraph::pie)'

%description
Apache keeps track of server activity in a structure known as the
I<scoreboard>.  There is a I<slot> in the scoreboard for each child
server, containing information such as status, access count, bytes
served and cpu time.  This same information is used by I<mod_status>
to provide current server statistics in a human readable form.

# %description -l pl
# TODO

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
%doc Changes README
%defattr(644,root,root,755)
%{perl_sitearch}/Apache/*.pm
%dir %{perl_sitearch}/auto/Apache/Scoreboard
%attr(755,root,root) %{perl_sitearch}/auto/Apache/Scoreboard/*.so
%{perl_sitearch}/auto/Apache/Scoreboard/*.bs
%dir %{perl_sitearch}/auto/Apache/DummyScoreboard
%attr(755,root,root) %{perl_sitearch}/auto/Apache/DummyScoreboard/*.so
%{perl_sitearch}/auto/Apache/DummyScoreboard/*.bs
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
