export type Employee = {
  id: string;
  name: string;
  role: "admin" | "employee";
  designation: string;
  avatarUrl?: string;
  status: "present" | "leave" | "absent";
};

export const employees: Employee[] = [
  { id: "1", name: "Aditi Sharma", role: "admin", designation: "HR Manager", status: "present" },
  { id: "2", name: "Rahul Verma", role: "employee", designation: "Software Engineer", status: "present" },
  { id: "3", name: "Priya Nair", role: "employee", designation: "UI Designer", status: "leave" },
  { id: "4", name: "Karan Mehta", role: "employee", designation: "Backend Developer", status: "absent" },
  { id: "5", name: "Sneha Iyer", role: "employee", designation: "QA Engineer", status: "present" },
  { id: "6", name: "Arjun Rao", role: "employee", designation: "DevOps Engineer", status: "leave" },
];