=head1 json-param-lib.pl

This module is based on the example module foobar. 
This is an example Webmin module for read or write json configuration file.

=cut

use WebminCore;
init_config();

use utf8;
use JSON;

=head2 get_params()

Returns a list of all json parameter file.

=cut
sub get_params
{
    my $file = $config{'json-param_conf'};
    my $json = do {
        open(my $json_fh, "<:encoding(UTF-8)", $file)
            or die("Can't open \$file\": $!\n");
        local $/;
        <$json_fh>
    };
    my $params = decode_json($json);
    return $params;
}

=head2 write_params(&parameters)

Write the parameter json file.

=cut
sub write_params
{
    my ($paramters) = @_;
    my $json = JSON->new;

    open my $fh, ">", $config{'json-param_conf'};
    print $fh $json->pretty->encode($paramters);
    close $fh;
}

=head2 apply_configuration()

Signal the  process to re-read it's configuration files.

=cut
sub apply_configuration
{
}
