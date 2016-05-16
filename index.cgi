#!/usr/bin/perl

# Show all json-param options
require 'json-param-lib.pl';

ui_print_header(undef, $module_info{'desc'}, "", undef, 1, 1);

# Build table contents
my $params = &get_params();
my @table = ();

while( my( $key, $value ) = each %$params ) {
    push(@table, [ "<a href='edit.cgi?name=".urlize($key).
                   "'>".html_escape($key)."</a>",
                   html_escape($value)
                 ]);
}

# Show the table with add links
print ui_form_columns_table(
        undef,
        undef,
        0,
        [ [ 'edit.cgi?new=1', $text{'index_add'} ] ],
        undef,
        [ $text{'index_name'}, $text{'index_value'} ],
        100,
        \@table,
        undef,
        0,
        undef,
        $text{'index_none'},
        );

ui_print_footer('/', $text{'index'});
