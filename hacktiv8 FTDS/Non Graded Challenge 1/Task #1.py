customer_id = ['B818', 'A461', 'A092', 'A082', 'B341', 'A005', 'A092', 'A461','B219',
             'B904', 'A901', 'A083', 'B904', 'A092', 'B341', 'B821','B341', 'B821', 'B904', 'B818', 'A901', 'A083', 'B818', 'A082','B219', 'B219', 'A083', 'A901', 'A082', 'B341', 'B341', 'A083','A082', 'B219', 'B439', 'A461', 'A005', 'A901', 'B341', 'A082','A083', 'A461', 'A083', 'A901', 'A461', 'A083', 'A082', 'A083','B341', 'A901', 'A082', 'A461', 'B219', 'A083', 'B818', 'B821','A092', 'B341', 'A461', 'A092', 'A083', 'B821', 'A092']

unique_idsonly = []
unique_id = []
for i in range(len(customer_id)):
    if customer_id[i] in unique_idsonly:
        continue
    else: 
        unique_idsonly.append(customer_id[i])
# # for idsonly in unique_idsonly:
# #     unique_id.append([idsonly, 0])
# # for ids in customer_id:
# #     for i in range(len(unique_id)):
# #         if ids == unique_id[i][0]:
# #             unique_id[i][1] += 1

print(unique_idsonly)
print(unique_id)
print(len(unique_idsonly))


