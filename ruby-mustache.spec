%define pkgname mustache
Summary:	Logic-less templates
Summary(pl.UTF-8):	Szablony bez logiki
Name:		ruby-%{pkgname}
Version:	1.1.1
Release:	1
License:	MIT
#Source0Download: https://github.com/mustache/mustache/releases
Source0:	https://github.com/mustache/mustache/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	73be40dd1b7a1fefe06dbf94845aac01
Group:		Development/Languages
URL:		http://mustache.github.io/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby >= 1:2.0
BuildRequires:	ruby-rdoc >= 4.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language."

%description -l pl.UTF-8
Mustache to zainspirowany przez ctemplate oraz et, niezależny od
szkieletu sposób renderowania widoków bez logiki.

Podobnie jak ctemplate, "podkreśla oddzielenie logiki od prezentacji;
niemożliwe jest osadzenie logiki aplikacji w tym języku szablonów".

%package -n mustache
Summary:	Logic-less templates processor
Summary(pl.UTF-8):	Procesor szablonów bez logiki
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description -n mustache
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language."

%description -n mustache -l pl.UTF-8
Mustache to zainspirowany przez ctemplate oraz et, niezależny od
szkieletu sposób renderowania widoków bez logiki.

Podobnie jak ctemplate, "podkreśla oddzielenie logiki od prezentacji;
niemożliwe jest osadzenie logiki aplikacji w tym języku szablonów".

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla pakietu %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:2.0

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla pakietu %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla pakietu %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:2.0

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla pakietu %{pkgname}.

%prep
%setup -q -n mustache-%{version}

%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# make gemspec self-contained
ruby -r rubygems -e 'spec = eval(File.read("%{pkgname}.gemspec"))
	File.open("%{pkgname}-%{version}.gemspec", "w") do |file|
	file.puts spec.to_ruby_for_cache
end'

rdoc --ri --op ri lib
rdoc --op rdoc lib
%{__rm} ri/created.rid
%{__rm} ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{_bindir},%{_mandir}/man{1,5},%{ruby_ridir},%{ruby_rdocdir}}

cp -a bin/* $RPM_BUILD_ROOT%{_bindir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

install -d $RPM_BUILD_ROOT
cp -a man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
cp -a man/*.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.md LICENSE README.md
%{ruby_vendorlibdir}/mustache.rb
%{ruby_vendorlibdir}/mustache
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files -n mustache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustache
%{_mandir}/man1/mustache.1*
%{_mandir}/man5/mustache.5*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mustache
