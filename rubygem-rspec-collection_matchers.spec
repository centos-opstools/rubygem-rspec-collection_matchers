# Generated from rspec-collection_matchers-1.1.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name rspec-collection_matchers

Name:             rubygem-%{gem_name}
Version:          1.1.3
Release:          2%{?dist}
Summary:          rspec-collection_matchers-1.1.3
Group:            Development/Languages
License:          MIT
URL:              https://github.com/rspec/rspec-collection_matchers
Source0:          https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:    ruby(release)
BuildRequires:    rubygems-devel
BuildRequires:    ruby
BuildRequires:    rubygem(rspec-expectations) >= 3

Requires:         rubygem(rspec-expectations) >= 3

BuildArch: noarch
%if 0%{?rhel}
Provides:         rubygem(%{gem_name}) = %{version}
%endif

%description
Collection cardinality matchers, extracted from rspec-expectations.


%package doc
Summary:          Documentation for %{name}
Group:            Documentation
Requires:         %{name} = %{version}-%{release}
BuildArch:        noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%{gem_instdir}/.rspec
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/features
%{gem_libdir}
%{gem_instdir}/script
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/Changelog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/rspec-collection_matchers.gemspec
%{gem_instdir}/spec

%changelog
* Mon Jan 30 2017 Martin Mágr <mmagr@redhat.com> - 1.1.3-2
- Fixed RHEL conditional

* Mon Jan 30 2017 Martin Mágr <mmagr@redhat.com> - 1.1.3-1
- Initial package
