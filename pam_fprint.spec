Name: pam_fprint
Version: 0.2
Release: %mkrel 1
Source: http://prdownloads.sourceforge.net/fprint/pam_fprint-%{version}.tar.bz2
Summary: Simple PAM module for fingerprint authentication.
License: GPL
Group: System/Libraries
BuildRequires: libfprint-devel pam-devel

%description
pam_fprint is a simple PAM module which uses libfprint's fingerprint processing
and verification functionality for authentication. In other words, instead of
seeing a password prompt, you're asked to scan your fingerprint.

pam_fprint is a proof-of-concept, and also my-first-PAM-module. It has some
deficiencies:

    * Can't be configured in any way.
    * Finds the first enrolled fingerprint that can be verified on a device
      that is currently plugged in, and uses that one and only that one.
    * Reads enrolled fingerprints from users home directories.
	  o It will only work when trying to authenticate your own user account
            (as you can read your own home directory), or in the system login
            prompt (which runs as root).
	  o You cannot authenticate yourself as another user, since you don't
            have access to read that user's home directory. 

To use pam_fprint, you must run pam_fprint_enroll to enroll (scan) your 
finger(s).

%prep
%setup -q

%build
%configure
%make

%install
rm -Rf %{buildroot}
%makeinstall_std
[ "lib" != "%{_lib}" ] && mv %{buildroot}/lib %{buildroot}/%{_lib}

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
/%{_lib}/security/pam_*.so
%{_bindir}/pam_fprint_enroll
%doc README ChangeLog NEWS
