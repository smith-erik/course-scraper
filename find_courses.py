import os
import sys
import json
import argparse


def main():
    parser = argparse.ArgumentParser(description='Find courses in scraped '
                                                 'data.')
    parser.add_argument('course_data_path', help='JSON file with course data')
    args = parser.parse_args()

    if not os.path.isfile(args.course_data_path):
        print("File '{}' not found.".format(args.course_data_path))
        sys.exit(1)
    with open(args.course_data_path, 'r+') as f:
        data = json.load(f)

    credits_list = [2]
    credits_set = frozenset(credits_list)

    course_list = [entry for entry in data
                   if int(entry['credits']) in credits_set
                   and entry['period'].lower() == 'fall']
    print_courses(course_list)
    sys.exit(0)


def print_courses(item_list):
    item_list = sorted(item_list, key=lambda x: x['code'])
    if len(item_list) != 0:
        for item in item_list:
            print_course(item)
            # print()
    else:
        print("List has no items.")


def print_course(item):
    print('{} - {}\n{} - {}'.format(item['code'], item['name'],
                                    item['credits'], item['period']))


if __name__ == '__main__':
    main()
