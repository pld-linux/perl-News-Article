#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	News
%define	pnam	Article
Summary:	News::Article Perl module
Summary(cs):	Modul News::Article pro Perl
Summary(da):	Perlmodul News::Article
Summary(de):	News::Article Perl Modul
Summary(es):	Módulo de Perl News::Article
Summary(fr):	Module Perl News::Article
Summary(it):	Modulo di Perl News::Article
Summary(ja):	News::Article Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	News::Article ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul News::Article
Summary(pl):	Modu³ Perla News::Article
Summary(pt):	Módulo de Perl News::Article
Summary(pt_BR):	Módulo Perl News::Article
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl News::Article
Summary(sv):	News::Article Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl News::Article
Summary(zh_CN):	News::Article Perl Ä£¿é
Name:		perl-News-Article
Version:	1.27
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	perl-PGP-Sign
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Article is a module for handling Usenet articles in mail or news
form.

%description -l pl
News::Article jest modu³em przeznaczonym do pracy z artyku³ami grup
dyskusyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/News/*.pm
%{_mandir}/man3/*
