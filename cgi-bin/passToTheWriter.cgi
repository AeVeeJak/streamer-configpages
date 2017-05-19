#!/usr/bin/perl -wT
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);

print header;
print start_html("Thank You");

$essid = param('ESSID');
$passwd = param('PASSWORD');

# need to untaint $essid and $passwd
if ($essid =~ m/([[:print:]]+)/) {
  $essid = $1;
} else {
  die "invalid essid";
};

if ($passwd =~ m/([[:print:]]+)/) {
  $passwd = $1;
} else {
  die "invalid password";
};

# call writeInterfaces with $essid and $passwd as arguments
@arguments = ($essid, $passwd);
$writeInterfaces = "/usr/bin/writeInterfaces";
$result = system($writeInterfaces, @arguments);

# hopefully that worked and we'll see the output now:
print $result

print h1("Thank you");

print end_html;
