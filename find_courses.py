import os
import sys
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description='Find courses in scraped '
                                                 'data.',
                                     epilog='Note that only fall courses '
                                            'are shown and that results are '
                                            'sorted first by credits and then '
                                            'by code.')
    parser.add_argument('course_data_path', help='JSON file with course data')
    parser.add_argument('-f', dest='credits_list', default=None, nargs='+',
                        help='only show courses with listed credits')
    parser.add_argument('-p', default=False, action='store_true',
                        dest='print_to_file', help='print output to file')
    args = parser.parse_args()

    if not os.path.isfile(args.course_data_path):
        print("File '{}' not found.".format(args.course_data_path))
        sys.exit(1)
    with open(args.course_data_path, 'r+') as f:
        data = json.load(f)

    if args.credits_list is not None:
        credits_set = frozenset(args.credits_list)
        course_list = [entry for entry in data
                       if entry['credits'] in credits_set
                       and entry['period'].lower() == 'fall']
    else:
        course_list = [entry for entry in data
                       if entry['period'].lower() == 'fall']
    
    if args.print_to_file == False:
        print("dpadpowka")
        print_courses(course_list)
    else:
        outfile = open('latest_search_results.txt', 'w+')
        print_courses(course_list, stream=outfile)
        outfile.close()
    sys.exit(0)


def print_courses(item_list, stream=None):
    item_list = sorted(item_list, key=lambda x: (x['credits'], x['code']))
    if len(item_list) != 0:
        for item in item_list:
            print_course(item, stream)
    else:
        print("List has no items.")


def print_course(item, stream=None):
    print('{:>14} - {:<2}- {}'.format(item['code'], item['credits'],
                                   item['name']), file=stream)


if __name__ == '__main__':
    main()
