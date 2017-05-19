#!/usr/bin/perl -w

use strict;
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use File::Basename;
use Archive::Extract;

my $upload_dir = "/opt/Streamer";
my $updateTar = param('roonUpdate');

print header;
print start_html;

if (!$updateTar) {
  print "There was a problem uploading your file.";
  exit;
}

my ($filename) = fileparse($updateTar);
print "Uploaded " . $filename . "<br>";

if ($filename =~ m/(RoonUpdate)-[0-9]{2}\.[0-9]{2}/) {
  $filename = $1;
} else {
  die "Filename contains invalid characters.";
}

my $upload_filehandle = upload("roonUpdate");

open (UPLOADFILE, ">", "$upload_dir/$filename.tar.gz") or die "Couldn't open destination file.";
binmode UPLOADFILE;

while (<$upload_filehandle>) {
  print UPLOADFILE;
}

close UPLOADFILE or die "Couldn't close destination file.";

print "File written to " . $upload_dir . "/" . $filename . ".tar.gz<br>";
print "Unpacking files<br>";
my $tarball = Archive::Extract->new( archive => "$upload_dir/$filename.tar.gz" );
my $untar = $tarball->extract( to => '/opt/Streamer' ) or die $tarball->error;

#system ("/bin/bash -xc /opt/Streamer/unpackUpdate.sh");
#print $? >> 8;

print "Done.<br> Please reboot your system. <br>";

print "<a href=\"../index.aevee.html\" title=\"Return to Streamer Homepage\">Home</a><br>";
print end_html;
