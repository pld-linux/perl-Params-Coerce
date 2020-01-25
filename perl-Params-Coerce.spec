#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Params
%define	pnam	Coerce
Summary:	Params::Coerce - allows your classes to do coercion of parameters
Summary(pl.UTF-8):	Params::Coerce - umożliwienie klasom jawnej kowersji typów parametrów
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
a variety of different arguments, while adding negligible additional
complexity to your code.

"Coercion" in computing terms generally refers to "implicit type
conversion". This is where data and object are converted from one type
to another behind the scenes, and you just just magically get what you
need.

%description -l pl.UTF-8
Dużą częścią dobrego projektu API jest możliwość elastycznego
przekazywania parametrów.

Params::Coerce próbuje zachęcić do tego poprzez ułatwianie
przyjmowania różnych argumentów przy zaniedbywalnie małej komplikacji
kodu.

"Coercion" oznacza "domyślną konwersję typów". Dotyczy to sytuacji,
kiedy dane i obiekty są w tle konwertowane z jednego typu do innego i
magicznie otrzymuje się to, co potrzeba.

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
%{perl_vendorlib}/Params/Coerce.pm
%{_mandir}/man3/Params::Coerce.3pm*
