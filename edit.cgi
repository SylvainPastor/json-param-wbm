#!/usr/bin/perl
# Show a form to create or edit a json-param options
require 'json-param-lib.pl';
ReadParse();

my $disabled;
my $name;
my $value;

# Show page header and get the site being edited
if ($in{'new'}) {
    ui_print_header(undef, $text{'create_title'}, "");
}
else {
    $disabled = 1; # Change the parameter name is not allowed
    ui_print_header(undef, $text{'edit_title'}, "");
    my $params = &get_params();
    $name  = $in{'name'};
    $value = $params->{$name};
}

# Generate form and inputs table start
print ui_form_start('save.cgi');
print ui_hidden('new', $in{'new'});
print ui_hidden('old', $in{'name'});
print ui_table_start($text{'edit_header'}, undef, 2);

################################################################

# Input for parameter name
print ui_table_row($text{'edit_name'},
    ui_textbox('name', $name, 32, $disabled));

# Input for parameter value
print ui_table_row($text{'edit_value'},
    ui_textbox('value', $value, 32));

################################################################

# Show buttons at the end of the form
print ui_table_end();
if ($in{'new'}) {
    print ui_form_end([ [ undef, $text{'create'} ] ]);
}
else {
    print ui_form_end([ [ undef, $text{'save'} ],
        [ 'delete', $text{'delete'} ] ]);
}

ui_print_footer('', $text{'index_return'});
