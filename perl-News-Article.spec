#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	News
%define	pnam	Article
Summary:	News::Article Perl module
Summary(cs):	Modul News::Article pro Perl
Summary(da):	Perlmodul News::Article
Summary(de):	News::Article Perl Modul
Summary(es):	M�dulo de Perl News::Article
Summary(fr):	Module Perl News::Article
Summary(it):	Modulo di Perl News::Article
Summary(ja):	News::Article Perl �⥸�塼��
Summary(ko):	News::Article �� ����
Summary(nb):	Perlmodul News::Article
Summary(pl):	Modu� Perla News::Article
Summary(pt):	M�dulo de Perl News::Article
Summary(pt_BR):	M�dulo Perl News::Article
Summary(ru):	������ ��� Perl News::Article
Summary(sv):	News::Article Perlmodul
Summary(uk):	������ ��� Perl News::Article
Summary(zh_CN):	News::Article Perl ģ��
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

%description -l pl
News::Article jest modu�em przeznaczonym do pracy z artyku�ami grup
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
