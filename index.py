import click
import classes


@click.command()
@click.option('--shard', default=None, help='shard number to query.')
def main(shard):

    if shard:
        classes.MerakiMethods.get_shard(shard)
    else:
        classes.MerakiMethods.get_all_shards()



if __name__ == '__main__':
    main()