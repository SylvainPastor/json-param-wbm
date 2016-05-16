#!/usr/bin/perl
# Create, update or delete a json-param option
require 'json-param-lib.pl';
ReadParse();

error_setup($text{'save_err'});
lock_file($config{'json-param_conf'});

my $name, $value;
my $params = &get_params();

# Get the old site object
if (!$in{'new'}) {
    $value = $params->{$in{'old'}};
    $value || &error(&text('save_egone',$in{'old'}));
}

if ($in{'delete'}) {
    # Just delete it
    delete $params->{$in{'old'}};
}
else {
    # Update or create
    $value = $in{'value'};

    # feature: Change the parameter name is not allowed
    if (not defined $in{'name'}) {
        $name = $in{'old'};
    } else {
        $name = $in{'name'};
    }

    # Validate inputs
    $name =~ /^[a-z0-9\.\-\_]+$/i ||
        error($text{'save_ename'});
    $value =~ /^[a-z0-9\.\-\_]+$/i ||
        error($text{'save_evalue'});

    $params->{$name} = $value;
}

write_params($params);
unlock_file($config{'json-param_conf'});
apply_configuration();

# Log the change
webmin_log(
    $in{'new'} ? 'create' : 
    $in{'delete'} ? 'delete' : 'modify', 
    'parameter', 
    $name.":".$value);

&redirect('');
