#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Params
%define	pnam	Coerce
Summary:	Params::Coerce - Allows your classes to do coercion of parameters
Summary(pl.UTF-8):	Params::Coerce - umożliwia klasom na wykonanie jawnej kowersji typów
Name:		perl-Params-Coerce
Version:	0.14
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Params/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a8439ea6777c9156424ef6dd74c83945
URL:		http://search.cpan.org/dist/Params-Coerce/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Params-Util >= 0.05
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A big part of good API design is that we should be able to be flexible
in the ways that we take parameters.

Params::Coerce attempts to encourage this, by making it easier to take
a variety of different arguments, while adding negligable additional
complexity to your code.

"Coercion" in computing terms generally referse to "implicit type
conversion". This is where data and object are converted from one type
to another behind the scenes, and you just just magically get what you
need.

The overload pragma, and its string overloading is the form of
coercion you are most likely to have encountered in Perl programming.
In this case, your object is automatically (within perl itself)
coerced into a string.

Params::Coerce is intended for higher-order coercion between various
types of different objects, for use mainly in subroutine and (mostly)
method parameters, particularly on external APIs.

%description -l pl.UTF-8
Dużą częścią dobrego projektu API jest możliwość elastycznego
przekazywania parametór.

Params::Coerce próbuję zachęcić do tego poprzez ułatwianie
przyjmowania różnych argumentów.

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
%doc Changes README
%{perl_vendorlib}/Params/*.pm
#%dir %{perl_vendorlib}/Params/Coerce
%{_mandir}/man3/*
