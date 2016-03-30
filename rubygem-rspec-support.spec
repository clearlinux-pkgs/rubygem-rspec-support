#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-rspec-support
Version  : 3.3.0
Release  : 9
URL      : https://rubygems.org/downloads/rspec-support-3.3.0.gem
Source0  : https://rubygems.org/downloads/rspec-support-3.3.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc

%description
# RSpec::Support
`RSpec::Support` provides common functionality to `RSpec::Core`,
`RSpec::Expectations` and `RSpec::Mocks`. It is considered
suitable for internal use only at this time.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n rspec-support-3.3.0
gem spec %{SOURCE0} -l --ruby > rubygem-rspec-support.gemspec

%build
gem build rubygem-rspec-support.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
rspec-support-3.3.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/rspec-support-3.3.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/Changelog.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/LICENSE.txt
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/caller_filter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/differ.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/directory_maker.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/encoded_string.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/fuzzy_matcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/hunk_generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/matcher_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/method_signature_verifier.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/object_formatter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/recursive_const_methods.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/ruby_features.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/deprecation_helpers.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/formatting_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/in_sub_process.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/library_wide_checks.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/shell_out.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/stderr_splitter.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/string_matcher.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/with_isolated_directory.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/spec/with_isolated_stderr.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/version_checker.rb
/usr/lib64/ruby/gems/2.3.0/gems/rspec-support-3.3.0/lib/rspec/support/warnings.rb
/usr/lib64/ruby/gems/2.3.0/specifications/rspec-support-3.3.0.gemspec
