%include	/usr/lib/rpm/macros.perl
%define	pdir	News
%define	pnam	Article
Summary:	News-Article perl module
Summary(pl):	Modu³ perla News-Article
Name:		perl-News-Article
Version:	1.13
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl-PGP-Sign
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News-Article is a module for handling Usenet articles in mail or news
form.

%description -l pl
News-Article jest modu³em przeznaczonym do pracy z artyku³ami grup
dyskusyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/News/*.pm
%{_mandir}/man3/*
