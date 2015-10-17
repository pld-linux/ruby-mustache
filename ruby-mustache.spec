# TODO:
# - warning: Installed (but unpackaged) file(s) found:
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel.rb
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel/mustache_extension.rb
#   /usr/lib/ruby/1.9/rack/bug/panels/mustache_panel/view.mustache

%define pkgname mustache
Summary:	Logic-less templates
Name:		ruby-%{pkgname}
Version:	0.11.2
Release:	2
License:	MIT
Source0:	http://github.com/defunkt/mustache/tarball/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	fc6e868cf09d40eaf36ffabaf1f412c4
Group:		Development/Languages
URL:		http://mustache.github.com/
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language."

%package -n mustache
Summary:	Logic-less templates processor
Group:		Applications/Publishing
Requires:	%{name} = %{version}-%{release}

%description -n mustache
Inspired by ctemplate and et, Mustache is a framework-agnostic way to
render logic-free views.

As ctemplates says, "It emphasizes separating logic from presentation:
it is impossible to embed application logic in this template
language."

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -qc
mv defunkt-mustache-*/* .

%{__sed} -i -e '1 s,#!.*ruby,#!%{__ruby},' bin/*

%build
# make gemspec self-contained
ruby -r rubygems -e 'spec = eval(File.read("%{pkgname}.gemspec"))
	File.open("%{pkgname}-%{version}.gemspec", "w") do |file|
	file.puts spec.to_ruby_for_cache
end'

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/Object
rm -r ri/lib/rack
rm ri/created.rid
rm ri/cache.ri

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
%doc CONTRIBUTORS HISTORY.md README.md
%{ruby_vendorlibdir}/mustache.rb
%{ruby_vendorlibdir}/mustache
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%if 0
# not packaging, don't want to pull rack as dep
%{ruby_vendorlibdir}/rack/bug/panels/mustache_panel.rb
%{ruby_vendorlibdir}/rack/bug/panels/mustache_panel
%endif

%files -n mustache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mustache
%{_mandir}/man1/%{pkgname}.1*
%{_mandir}/man5/%{pkgname}.5*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Mustache
%{ruby_ridir}/Rack
