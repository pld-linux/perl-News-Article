#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	News
%define		pnam	Article
Summary:	News::Article Perl module
Summary(cs.UTF-8):	Modul News::Article pro Perl
Summary(da.UTF-8):	Perlmodul News::Article
Summary(de.UTF-8):	News::Article Perl Modul
Summary(es.UTF-8):	Módulo de Perl News::Article
Summary(fr.UTF-8):	Module Perl News::Article
Summary(it.UTF-8):	Modulo di Perl News::Article
Summary(ja.UTF-8):	News::Article Perl モジュール
Summary(ko.UTF-8):	News::Article 펄 모줄
Summary(nb.UTF-8):	Perlmodul News::Article
Summary(pl.UTF-8):	Moduł Perla News::Article
Summary(pt.UTF-8):	Módulo de Perl News::Article
Summary(pt_BR.UTF-8):	Módulo Perl News::Article
Summary(ru.UTF-8):	Модуль для Perl News::Article
Summary(sv.UTF-8):	News::Article Perlmodul
Summary(uk.UTF-8):	Модуль для Perl News::Article
Summary(zh_CN.UTF-8):	News::Article Perl 模块
Name:		perl-News-Article
Version:	1.27
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	77a49112a1ec680d4c4eeddcdfbca32c
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	perl-PGP-Sign
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
News::Article is a module for handling Usenet articles in mail or news
form.

%description -l pl.UTF-8
News::Article jest modułem przeznaczonym do pracy z artykułami grup
dyskusyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/News/*.pm
%{_mandir}/man3/*
