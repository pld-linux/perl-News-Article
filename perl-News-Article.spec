%include	/usr/lib/rpm/macros.perl
Summary:	News-Article perl module
Summary(pl):	Modu³ perla News-Article
Name:		perl-News-Article
Version:	1.13
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/News/News-Article-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-libnet
BuildRequires:	perl-PGP-Sign
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News-Article is a module for handling Usenet articles in mail or news
form.

%description -l pl
News-Article jest modu³em przeznaczonym do pracy z artyku³ami grup
dyskusyjnych.

%prep
%setup -q -n News-Article-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/News/Article
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/News/*.pm
%{perl_sitearch}/auto/News/Article

%{_mandir}/man3/*
